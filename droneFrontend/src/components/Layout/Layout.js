import axios from "axios";
import React, { useEffect, useRef, useState } from "react";
import { Button, ProgressBar } from "react-bootstrap";
import DroneTable from "../DroneTable/DroneTable";

import Map from '../Map/Map';
import MapService, { MAPBOX_ACCESS_TOKEN } from '../Map/MapService';
import Overlay from "../Overlay/Overlay";
import UploadOverlay from "../UploadOverlay/UploadOverlay";
import './Layout.css';

export default function Layout() {

    const mapService = useRef(null);
    const cnn=useRef([0,0]);
    const droneJsonData=useRef(null);

    let [ invisibility, setInvisibility ] = useState('Hide');
    let [ progressBarVisibility, setProgressBarVisibility ] = useState('Hide');
    let [ uploadedPercent, changeUploadedPercent ] = useState(0);

    let overlayMonitor = e => {
        if(!invisibility){
            setInvisibility('Hide')
        }else
            setInvisibility('');
    };

    let ProgressBarVisibilityMonitor = e =>{
        if(!progressBarVisibility){
            setProgressBarVisibility('Hide')
        }else
            setProgressBarVisibility('');
    };

    let uploadFile=()=>{
        console.log(droneJsonData.current, 'uploaded')
        setProgressBarVisibility();
        let data=new FormData();
        data.append('file', JSON.stringify(droneJsonData.current));
        changeUploadedPercent(0);
        const options={
            onUploadProgress: progressEvent=>{
                let percent=Math.floor((progressEvent.loaded/progressEvent.total)*100);
                changeUploadedPercent(percent)
                console.log(progressEvent, uploadedPercent)
            }
        }

        axios.post('http://localhost:8000/dronedata/', data, options).then(res=>{
            // console.log(res);
            // changeUploadedPercent(0);
        })
        return;
    }

    useEffect(() => {
        //initialize only once
        if (mapService.current) {
            return;
        }
        //mapservice set to hook which is map object
        const mapObj = new MapService();
        mapObj.initMap();
        mapService.current = mapObj;
        console.log('has been rendered');
    }, []);

    // //function defination of the bounded box drawn by user
    function getBoundingBox() {
        const bbox = mapService.current.getdrawnBoundingBox();
        if (!bbox) {
            return;
        }
        console.log('Drawn bbox:', bbox)
        alert('Drawn bbox coordinatessssssssssssssssssssssss: ' + JSON.stringify(bbox.geometry.coordinates));
    }

    return (
        <div className='layout'>
            <Overlay droneJsonData={droneJsonData} invisibility={invisibility} setInvisibility={overlayMonitor} mapService={mapService} />
            <UploadOverlay
             visibility={progressBarVisibility} 
             setProgressBarVisibility={ProgressBarVisibilityMonitor} 
             uploadedPercent={uploadedPercent} />
            <div className='layout__content_cont'>
                <div style={{padding:'1em',display:'flex', justifyContent:'space-evenly'}}>
                    <Button variant="success" onClick={(e)=>overlayMonitor(e)}>
                        Add JSON File
                    </Button>
                    <Button variant="success" onClick={uploadFile}>
                        Upload
                    </Button>
                </div>
                <DroneTable drones={droneJsonData}/>
                <div>
                    <button onClick={getBoundingBox}>
                        Get bounding box coordinate
                    </button>
                    <p>Note: Check console for full object</p>
                </div>
            </div>

            <div className='layout__map_cont'>
                {MAPBOX_ACCESS_TOKEN && <Map />}
            </div>

        </div>
    );
};
