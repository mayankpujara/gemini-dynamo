import React from "react";

function Flashcard({term, definition, onDiscard}){   
    console.log("Flashcard Props", {term, definition});
    return(
        <div className="flashcard">
            <div className="content">
                <h3>{term}</h3>
                <p>{definition}</p>
            </div>
            <button onClick={onDiscard} className="Discard">
                Discard
            </button>
        </div>
    );
}

export default Flashcard;