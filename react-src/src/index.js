import React from "react";
import ReactDOM from "react-dom";
import App from "./App"; // Hier wird App.js importiert

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root") // Rendert die App in den div mit der ID "root"
);
