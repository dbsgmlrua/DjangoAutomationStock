import React from 'react';
import useGetAxios from './useAxios';

const Home = () => {
    const {data, isPending, error} = useGetAxios('/hello/');

    return ( 
        <div>
            <h2>{isPending && <div>Loading..</div>}</h2>
            <h2>{error && <div>{error}</div>}</h2>
            <h2>{data && data.hello}</h2>
        </div>
     );
}
 
export default Home;