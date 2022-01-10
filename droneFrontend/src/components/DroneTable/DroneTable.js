import { Table } from 'react-bootstrap';
import ReactPaginate from 'react-paginate'
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from "react";
import Auxil from '../Auxil/Auxil';
import Row from '../Row/Row';

export default function DroneTable(props) {
    const [nameFilter, setNameFilter] = useState("");
    const [brandFilter, setBrandFilter] = useState("");
    const [currentPage, setCurrentPage] = useState(0);

    const startOffset=currentPage*props.itemsPerPage;
    const endOffset=startOffset+props.itemsPerPage;
    console.log(startOffset,endOffset);

    let deletevalue = (index) => {
        console.log('at index', index)
        props.drones.current.splice(index, 1);
        props.setElementDeleted(props.elementDeleted + 1);
    };

    let rowOfItems=null;
    if(!(props.drones.current===null || props.drones.current===[])){
        rowOfItems=props.drones.current.map((e, i)=>{
            if (e.drone_name.toLowerCase().includes(nameFilter.toLowerCase()) === true && e.drone_type.model_name.toLowerCase().includes(brandFilter.toLowerCase()) === true) {
                return { drone: e, ogIndex: i };
            }else
                return null;
            
        }).filter(e => e!==null );
    };
    console.log(rowOfItems);
    let droneDataSerializer = () => {
        if(!rowOfItems)
            return null;
        return rowOfItems.map((e,i) => <Row
                                         rowData={e}
                                         deletevalue={deletevalue} 
                                         invisibilityClass={ (i>=startOffset && i<endOffset) ? '' : 'Hide' } />);
    };
    let pageChange = e =>{
        console.log(e);
        setCurrentPage(e.selected)
    };
    if (props.drones.current) {
        if (props.drones.current.length === 0)
            return null;
        return (
            <Auxil>
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <input type={'text'} placeholder='Drone Name' value={nameFilter} onChange={e => setNameFilter(e.target.value)} />
                    <input type={'text'} placeholder='Drone Brand' value={brandFilter} onChange={e => setBrandFilter(e.target.value)} />
                </div>
                <div style={{ maxHeight: '20rem', overflowY: 'scroll', scrollbarWidth: 'none' }}>
                    <Table variant="dark" style={{ height: '100%' }}>
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
                </div>
                <ReactPaginate 
                    pageRangeDisplayed={2}
                    activeClassName={'active'}
                    breakLinkClassName={'page-link'}
                    pageLinkClassName={'page-link'}
                    breakLabel={'...'}
                    pageClassName={'page-item'}
                    previousLinkClassName={'page-link'}
                    nextClassName={'page-item'}
                    nextLinkClassName={'page-link'}
                    breakClassName={'page-item'}
                    previousClassName={'page-item'}
                    containerClassName='pagination'
                    pageCount={Math.ceil(props.drones.current.length/props.itemsPerPage)}
                    nextLabel={'next'}
                    previousLabel={'previous'}
                    onPageChange={pageChange}
                />
                <div>Element Deleted : {props.elementDeleted}</div>
            </Auxil>
        )
    } else {
        return null;
    }
}