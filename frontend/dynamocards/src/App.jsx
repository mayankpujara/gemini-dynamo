import React, {useState} from "react";
import axios from "axios";
import Flashcard from "./Flashcard.jsx";
import './style.css'

function App(){
  const [youtubeLink, setYoutubeLink] = useState("");
  const [keyConcepts, setKeyConcepts] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleLinkChange = (event) => {
    console.log(event.target.value)
    setYoutubeLink(event.target.value);
  };

  const sendLink = async () => {
    setIsLoading(true);

    try {
      const response = await axios.post("http://localhost:8000/analyse_video", {
        youtube_link: youtubeLink,
      });

      const data = response.data

      if (data.key_concepts && Array.isArray(data.key_concepts)) {
        setKeyConcepts(data.key_concepts);
      }
      else{
        console.error("Data does not contain key concepts:", data);
        console.log(data.key_concepts)
        setKeyConcepts([]);
      }
      
    } catch (error){
      console.log(error);
      setKeyConcepts([]);
    }
    finally{
      setIsLoading(false);
    }
  };

  const discardFlashCard = (index) => {
    setKeyConcepts(currentConcepts => currentConcepts.filter((_, i) => i != index));
  }


  return (
    <div className="root">
      <h1 className="heading">Welcome to Dynamo Cards 👋</h1>
      <hr></hr>
    <div className="App">
      <div className="Cards">      
        <h1>FlashCards Generator</h1> 
        <h3>Creates flash cards from a YouTube video URL</h3>
      <div className="inputContainer">
        <input
          type = "text"
          placeholder = "Paste Youtube URL here"
          value = {youtubeLink}
          onChange = {handleLinkChange}
          className="inputField"
        />
        <button onClick={sendLink} disable={isLoading} className="Generate">
          {isLoading ? 'Loading..': 'Generate Flashcards'}
        </button>
      </div>
      <div className="flashcardsContainer">
        {keyConcepts.map((concept, index) => (
          <Flashcard
            key ={index}
            term = {concept.term}
            definition = {concept.definition}
            onDiscard ={() => discardFlashCard(index)}
          />
        ))}
      </div>
      </div>
    </div>
    </div>
  )
}

export default App;