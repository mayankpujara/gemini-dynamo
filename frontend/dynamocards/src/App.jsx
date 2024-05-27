import React, {useState} from "react";
import axios from "axios";
import Flashcard from "./Flashcard.jsx";
import './Flashcard.css'

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
        const transformed_concepts = data.key_concepts.map((concept) => {
          const term = Object.keys(concept)[0];
          const definition = concept[term];
          return {term, definition};
        });
      setKeyConcepts(transformed_concepts);
      }
      else{
        console.error("Data does not contain keyConcepts:", data);
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
    <div className="App">
      <h1>YouTube Link to Flashcards Generator</h1> 
      <div className="inputContainer">
        <input
          type = "text"
          placeholder = "Paste Youtube URL here"
          value = {youtubeLink}
          onChange = {handleLinkChange}
          className="inputField"
        />
        <button onClick={sendLink} disable={isLoading}>
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
  )
}

export default App;