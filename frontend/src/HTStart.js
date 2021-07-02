import React from 'react';

const HTStart = () => {
    const [loginForm, setLoginForm] = useState({id: "", pwd: "", pwdcert: ""})

    const handleEachInput = (e) => {
        const { id, value } = e.target;
        setLoginForm({...loginForm, [id]: value});
        console.log(loginForm);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        
        console.log(loginForm);
        axiosInstance.post('/token/obtain/', {
            id: loginForm.id,
            pwd: loginForm.pwd,
            pwdcert: loginForm.pwdcert
        }).then(
            result => {
                console.log(result.data);
                // axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access;
                // localStorage.setItem('access_token', result.data.access);
                // localStorage.setItem('refresh_token', result.data.refresh);
                // history.push('/');
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
                    placeholder="아이디"
                    className="login_input"
                    id="id"
                    onChange={handleEachInput}
                />
                <input
                    type="password"
                    placeholder="비밀번호"
                    className="password_input"
                    id="pwd"
                    onChange={handleEachInput}
                />
                <input
                    type="password"
                    placeholder="비밀번호"
                    className="password_input"
                    id="pwdcert"
                    onChange={handleEachInput}
                />
    
                <div>
                    <button onClick={handleSubmit} disabled={!activateBtn}>
                    로그인
                    </button>
                </div>
            </form>
        </div> 
     );
}
 
export default HTStart;