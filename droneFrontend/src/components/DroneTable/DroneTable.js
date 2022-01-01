import { Table } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from "react";
import Auxil from '../Auxil/Auxil';

export default function DroneTable(props){
    const [nameFilter, setNameFilter ] = useState('');
    const [brandFilter, setBrandFilter ] = useState('');
    const [dateFilter, setDateFilter ] = useState('');
    let deletevalue=(index)=>{
        // console.log('at index', index)
        props.drones.current.splice(index,1);
        props.setElementDeleted(props.elementDeleted+1);
        // props.mapService.current.addPoints(props.drones.current.map(e=>{
        //     // console.log(e)
        //     return [e.location.latitude, e.location.longitude]
        // }))

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
            <Auxil>
                <div style={{display:'flex',flexDirection:'column', alignItems:'center'}}>
                    <input type={'text'} placeholder='ID' value={nameFilter} onChange={e=>setNameFilter(e.target.value)} />
                    <input type={'text'} placeholder='Brand' value={brandFilter} onChange={e=>setBrandFilter(e.target.value)} />
                    <input type={'text'} placeholder='Date' value={dateFilter} onChange={e=>setDateFilter(e.target.value)} />
                </div>
                <div style={{maxHeight:'20rem',overflowY:'scroll',scrollbarWidth:'none'}}>
                    <Table variant="dark" style={{height:'100%'}}>
                        <thead>
                            {/* <tr>
                                <th><input type={'text'} placeholder='ID' value={null} /></th>
                                <th><input type={'text'} placeholder='ID' value={null} /></th>
                                <th><input type={'text'} placeholder='ID' value={null} /></th>
                                <th><input type={'text'} placeholder='ID' value={null} /></th>
                                <th>Delete</th>
                            </tr> */}
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
                    <div>Element Deleted : {props.elementDeleted}</div>
                </div>
            </Auxil>
        )
    }else{
        return null;
    }
}