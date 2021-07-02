import axiosInstance from "./axiosApi";
import { useState, useEffect } from "react";
import {useHistory} from 'react-router-dom';

const useGetAxios = (url) => {
    const [data , setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);
    const history = useHistory();

    useEffect(()=>{
        axiosInstance.get(url)
        .then(function (response){
            console.log(response.data);
            setData(response.data);
            setIsPending(false);
            setError(null);
        })
        .catch((err =>{
            setIsPending(false);
            setError(err.message);
        }));
    },[url]);

    return {data, isPending, error};
}

export default useGetAxios;