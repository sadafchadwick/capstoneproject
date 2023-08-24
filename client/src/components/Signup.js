import React, { useContext } from 'react';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { UserContext } from './UseContext';


function Signup() {

    const history = useHistory()

    const [userName, setUserName] = useState('')
    const [password, setPassword] = useState('')

    const { setUser } = useContext(UserContext)

    function handleSubmit(e) {
        e.preventDefault();
        const formObj = {
            'userName': userName,
            'password': password,
            'name': userName
        }

        fetch('http://127.0.0.1:5555/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formObj)
        })
            .then(r => {
                if (r.ok) {
                    r.json()
                        .then(data => {
                            history.push('/home')
                            setUser(data)
                        })
                }
                else {
                    r.json()
                        .then(data => {
                            console.log(data)
                        })
                }
            })
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                placeholder='Username'
                type="text"
                id="userName"
                value={userName}
                onChange={(e) => setUserName(e.target.value)}
            />

            <input
                placeholder='Password'
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <button type="submit">Signup</button>
        </form>
    )
}

export default Signup