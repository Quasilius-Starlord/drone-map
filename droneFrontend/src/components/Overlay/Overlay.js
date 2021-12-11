import './Overlay.css';
import './Content.css';
import './Hide.css';
import Auxil from './../Auxil/Auxil.js'
import { useState, useRef } from 'react';

export default function Overlay(props){
    let triggerhidden=null;
    const selectedFile=useRef(null);

    // const processState=useRef(false);
    const [currSelectedFile, changeSelectedFile]=useState(null);

    let processCurrSelected=()=>{
        if(currSelectedFile){
            const coordinate=currSelectedFile.slice(0,4).map((e, i)=>{
                return [e.location.latitude, e.location.longitude]
            })
            props.mapService.current.addPoints(coordinate);
            // setTimeout(()=>{
            //     props.setInvisibility(0);
            // },5000);
            return(
                <Auxil>
                    <div>Name: {selectedFile.current.name}</div>
                    <div>Name: {selectedFile.current.type}</div>
                    {currSelectedFile.slice(0,4).map((ele, i)=>{return (<div key={i}>{`${i+1}. Name ${ele.drone_name} ${ele.location.latitude},${ele.location.longitude}`}</div>)})}
                </Auxil>
            )
        }else{
            return(
                <div>No file selected</div>
            )
        }
    }

    return(
        <div className={`Background ${props.invisibility}`}
         onClick={e=>{
            if(triggerhidden===e.target)
                props.setInvisibility(e);
         }}
         ref={node=>{triggerhidden=node}} >
            <div className={`Content`}>
                Content
                <input type='file' onChange={e=>{
                    const fileReader = new FileReader();
                    fileReader.readAsText(e.target.files[0],'UTF-8');
                    //  file is in selectedfile
                    selectedFile.current=e.target.files[0];

                    //  json stored in the state
                    fileReader.onload=e=>{
                        changeSelectedFile(JSON.parse(e.target.result));
                        // selectedFile=
                    }
                }} accept='.json'/>
                {processCurrSelected()}
            </div>
        </div>
    )
};