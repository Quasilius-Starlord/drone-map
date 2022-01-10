import './Overlay.css';
import './Hide.css';
import './Content.css';
import Auxil from './../Auxil/Auxil.js'
import { useState, useRef } from 'react';
import axios from 'axios'

export default function Overlay(props){
    let triggerhidden=null;

    // const processState=useRef(false);
    const [currSelectedFile, changeSelectedFile]=useState(null);

    let processCurrSelected=()=>{
        if(currSelectedFile){
            return(
                <div>file Selected</div>
                // <Auxil>
                //     <div>Name: {selectedFile.current.name}</div>
                //     <div>Name: {selectedFile.current.type}</div>
                    // {/* {currSelectedFile.slice(0,4).map((ele, i)=>{return (<div key={i}>{`${i+1}. Name ${ele.drone_name} ${ele.location.latitude},${ele.location.longitude}`}</div>)})} */}
                // {/* </Auxil> */}
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
                    console.log('drone json', props.droneJsonData);
                    //  json stored in the state
                    fileReader.onload=e=>{
                        let jsonmapdata=JSON.parse(e.target.result);
                        changeSelectedFile(jsonmapdata);
                        props.droneJsonData.current=jsonmapdata;
                        props.setInvisibility(triggerhidden);
                    }
                    e.target.value='';
                }} accept='.json'/>
                {processCurrSelected()}
            </div>
        </div>
    )
};