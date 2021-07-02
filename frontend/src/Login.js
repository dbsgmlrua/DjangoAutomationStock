import React from 'react';
import axiosInstance from "./axiosApi";
import { useState } from "react";
import {useHistory} from 'react-router-dom';

const Login = () => {
    const [loginForm, setLoginForm] = useState({id: "", pw: ""})
    const [activateBtn, setActivateBtn] = useState(true);
    const history = useHistory();
    
    const handleEachInput = (e) => {
        const { id, value } = e.target;
        setLoginForm({...loginForm, [id]: value});
        console.log(loginForm);
    };
    const handleSubmit = (event) => {
        event.preventDefault();
        
        console.log(loginForm);
        axiosInstance.post('/token/obtain/', {
            username: loginForm.id,
            password: loginForm.pw
        }).then(
            result => {
                console.log(result.data);
                axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access;
                localStorage.setItem('access_token', result.data.access);
                localStorage.setItem('refresh_token', result.data.refresh);
                history.push('/');
            },
            error =>{
                throw error;
            }
        )
    };

    return ( 
    <div className="Login">
        <form>
            <input
                type="text"
                placeholder="전화번호, 사용자 이름 또는 이메일"
                className="login_input"
                id="id"
                onChange={handleEachInput}
            />
            <input
                type="password"
                placeholder="비밀번호"
                className="password_input"
                id="pw"
                onChange={handleEachInput}
            />

            <div>
                <button onClick={handleSubmit} disabled={!activateBtn}>
                로그인
                </button>
            </div>
        </form>
    </div> );
}
 
export default Login;