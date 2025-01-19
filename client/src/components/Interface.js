import React, {useState, useEffect, useRef} from 'react';
import '../styles/styles.css'
function Interface() {
    const [messages, setMessages] = useState([])
    
    const [inputText, setInputText] = useState('')

    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({behavior:"smooth"});
    };

    useEffect(scrollToBottom,[messages]);

    const handleSendQuery = async (event) => {
        event.preventDefault();
        if (!inputText.trim()) return;


        const body = {search_query: inputText}
        
        setMessages([...messages, {sender:"user", message:inputText}]);
        
        setInputText(''); 

        const response = await fetch('http://localhost:3000/get-search-kws',
            {
                method: 'POST',
                headers: {'Accept': 'application/json',
                    'Content-type':'application/json'},
                body: JSON.stringify(body),
            
            });
        const data = await response.json();
        setMessages(currentMessages => [...currentMessages, {sender:"bot", message:data.answer}])
        
    };

    return (
       <div className='chat-container'>
       <header className="chat-header">What would you like 
            to know about today's world events? </header>
        
        <div className="chat-messages">
            {messages.map((item)=> (
                <div>
                {item.sender === 'user'? <p align="right">{item.message}</p>:<p >{item.message}</p>}
                </div>
            ))}
        </div>
       <form className="chat-input" onSubmit={handleSendQuery}>
        <input
        type="text"
        placeholder="Type in a question or keywords. ex: United States"
        value={inputText}
        onChange={(e)=>setInputText(e.target.value)}
        />
       </form>
       </div>
    );
}

export default Interface;