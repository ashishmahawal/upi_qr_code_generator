import { UserInput } from "./components/UserInput/UserInput";
import { QRImage } from "./components/UserInput/QRImage";
import React from "react";
import { ImageContext } from "./storage/app-context";

function App() {
  return (
<ImageContext.Provider value= {{img:''}}>
  <UserInput/>
</ImageContext.Provider>

  );
}

export default App;
