import { Table } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState} from "react";
import Auxil from '../Auxil/Auxil';

export default function DroneTable(props){
    const [elementDeleted,setElementDeleted]=useState(0);
    let deletevalue=(index)=>{
        console.log('at index', index)
        props.drones.current.splice(index,1);
        setElementDeleted(elementDeleted+1);
    }
    let droneDataSerializer=()=>{
        return(<Auxil>
            {props.drones.current.map((e, i)=>{
                return(
                    <tr key={i}>
                        <td>{e.reg_id}</td>
                        <td>{e.drone_name}</td>
                        <td>{e.drone_type.model_name}</td>
                        <td>{e.pilot.name}</td>
                        <td><button style={{height:'30px',width:'50px',color:'black',backgroundColor:'red'}} onClick={()=>{deletevalue(i)}}>X</button></td>
                    </tr>
                )
            })}
        </Auxil>)
    };
    if(props.drones.current){
        if(props.drones.current.length===0)
            return null;
        return(
            <div style={{maxHeight:'20rem',overflowY:'scroll',scrollbarWidth:'none'}}>
                <Table variant="dark" style={{height:'100%'}}>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Brand</th>
                            <th>Pilot</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        {droneDataSerializer()}
                    </tbody>
                </Table>
                <div>Element Deleted : {elementDeleted}</div>
            </div>
        )
    }else{
        return null;
    }
}