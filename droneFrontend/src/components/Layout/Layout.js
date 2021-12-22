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

    const newdata=useRef([
        {
            "drone_name": "Ritvik",
            "reg_id": 1,
            "location": {
                "latitude": 26.027207835264562,
                "longitude": 85.05834646542837
            },
            "last_seen": "2021-02-20 01:11:37",
            "first_launch": "2021-02-02 13:43:52",
            "total_flight_time_min": 128,
            "drone_type": {
                "id": 37,
                "model_name": "Mini pro",
                "brand": "DJI",
                "model_year": "2016",
                "endurance_min": "24",
                "sl_no": "082-23-8151",
                "type": "quad"
            },
            "pilot": {
                "id": 3637,
                "name": "Rania Tak",
                "address": "702\nCheema Street\nBerhampore-250764",
                "phone": "07435013056",
                "experience": 1,
                "skill": 3,
                "country": "India"
            }
        },
        {
            "drone_name": "Aarush",
            "reg_id": 2,
            "location": {
                "latitude": 20.50261768211302,
                "longitude": 79.56760337007684
            },
            "last_seen": "2021-03-23 18:13:02",
            "first_launch": "2019-04-03 01:35:42",
            "total_flight_time_min": 302,
            "drone_type": {
                "id": 6,
                "model_name": "DJI Mavic v3",
                "brand": "DJI",
                "model_year": "2018",
                "endurance_min": "23",
                "sl_no": "282-62-3373",
                "type": "quad"
            },
            "pilot": {
                "id": 8382,
                "name": "Arnav Sura",
                "address": "84/303, Jhaveri Zila, Panvel 306201",
                "phone": "09246416699",
                "experience": 2,
                "skill": 1,
                "country": "India"
            }
        },
        {
            "drone_name": "Tiya",
            "reg_id": 3,
            "location": {
                "latitude": 23.89430689372223,
                "longitude": 75.4822003284608
            },
            "last_seen": "2021-03-18 02:42:27",
            "first_launch": "2020-03-13 16:40:37",
            "total_flight_time_min": 929,
            "drone_type": {
                "id": 41,
                "model_name": "Swinf pro 2",
                "brand": "Parrot",
                "model_year": "2020",
                "endurance_min": "120",
                "sl_no": "784-19-1278",
                "type": "vtol"
            },
            "pilot": {
                "id": 3631,
                "name": "Shalv Wagle",
                "address": "H.No. 87, Setty Ganj, Morena-429574",
                "phone": "08396022723",
                "experience": 1,
                "skill": 1,
                "country": "India"
            }
        }
    ]);

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
