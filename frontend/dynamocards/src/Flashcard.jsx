import React from "react";

function Flashcard({term, definition, onDiscard}){
    console.log("Flashcard Props", {term, definition});
    return(
        <div className="flashcard">
            <h3>{term}</h3>
            <p>{definition}</p>
            <button onClick={onDiscard} style={{marginTop: '10px'}}>
                Discard
            </button>
        </div>
    );
}

export default Flashcard;