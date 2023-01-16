import { getUPIQR } from "../../services/serverAPI";
import React, { useState, useEffect,useContext } from "react";
import { ImageContext } from "../../storage/app-context";
import { QRImage } from "./QRImage";
export function UserInput(props) {
  const [name, setName] = useState("");
  const [amount, setAmount] = useState("");
  const [upi_adr, setUPIAdr] = useState("");
  const [counter,refreshImage] = useState(0)
  let ImageContext_1 = useContext(ImageContext)
  const generateQR = async (event) => {
    event.preventDefault();
    
    let qrData = {
      name,
      amount,
      upi_adr,
    };
    const responseData = await getUPIQR(qrData);
    
    let qrImage = await responseData.blob()
    let imageUrl = URL.createObjectURL(qrImage)
    ImageContext_1.img = imageUrl
    refreshImage(counter+1)
  }
// useEffect(()=>{

// },[img])
  return (
    <div>
      <h1>UPI QR Code generator app!!!!</h1>
      <form>
        <label>Reciever's UPI Id</label>
        <input type="text" onChange={(e) => setUPIAdr(e.target.value)} />
        <br />
        <label>Amount to Recieve</label>
        <input type="text" onChange={(e) => setAmount(e.target.value)} />
        <br />
        <label>Reciever Name</label>
        <input type="text" onChange={(e) => setName(e.target.value)} />
        <br />
        <button type="submit" onClick={generateQR}>Get QR</button>
      </form>
<QRImage></QRImage>
    </div>
  );
}
