import { getUPIQR } from "../../services/serverAPI";
import React, { useState, useEffect, useContext } from "react";
import { ImageContext } from "../../storage/app-context";
import { QRImage } from "./QRImage";
import { TextField, Button,Typography } from "@mui/material/";
import "./UserInput.css"


export function UserInput(props) {
  const [name, setName] = useState("");
  const [amount, setAmount] = useState("");
  const [upi_adr, setUPIAdr] = useState("");
  const [counter, refreshImage] = useState(0);
  let ImageContext_1 = useContext(ImageContext);
  const generateQR = async (event) => {
    event.preventDefault();

    let qrData = {
      name,
      amount,
      upi_adr,
    };
    const responseData = await getUPIQR(qrData);

    let qrImage = await responseData.blob();
    let imageUrl = URL.createObjectURL(qrImage);
    ImageContext_1.img = imageUrl;
    refreshImage(counter + 1);
  };

  return (
    <div>
      <Typography variant="h2" component="h3">
      UPI QR Code generator
</Typography> <br />
      <div className="ashish">
        <TextField
          style={{ margin: "10px" }}
          label="Reciever's UPI Id"
          color="secondary"
          focused
          onChange={(e) => setUPIAdr(e.target.value)}
        />
        <TextField
          style={{ margin: "10px" }}
          label="Amount"
          color="secondary"
          focused
          onChange={(e) => setAmount(e.target.value)}
        />
        <TextField
          style={{ margin: "10px" }}
          label="Name"
          color="secondary"
          focused
          onChange={(e) => setName(e.target.value)}
        /> <br />
        <Button variant="contained" color="success" onClick={generateQR}>
          Get QR
        </Button>
      </div>

      <QRImage></QRImage>
    </div>
  );
}
