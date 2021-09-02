import React from 'react';
import useGetAxios from './useAxios';

const ExceptionTest = () => {
    const {data, isPending, error} = useGetAxios('/stock/exceptions');

    return ( 
        <div>
            <h2>{isPending && <div>Loading..</div>}</h2>
            <h2>{error && <div>{error}</div>}</h2>
            <h2>{data && data.message}</h2>
        </div>
     );
}
 
export default ExceptionTest;