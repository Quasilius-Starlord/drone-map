import { Table } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';


export default function DroneTable(props){

    let droneDataSerializer=()=>{
        return props.drones.current.map((e, i)=>{
            console.log(e);
            return(<tr>
                <td>{e.reg_id}</td>
                <td>{e.drone_name}</td>
                <td>{e.drone_type.model_name}</td>
                <td>{e.pilot.name}</td>
            </tr>)
        })
    };
    if(props.drones.current){
        return(
            <div style={{maxHeight:'20rem',overflowY:'scroll',scrollbarWidth:'none'}}>
                <Table variant="dark" style={{height:'100%'}}>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Brand</th>
                            <th>Pilot</th>
                        </tr>
                    </thead>
                    <tbody>
                        {droneDataSerializer()}
                    </tbody>
                </Table>
            </div>
        )
    }else{
        return null;
    }
}