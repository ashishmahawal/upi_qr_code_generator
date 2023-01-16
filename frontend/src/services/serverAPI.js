//const ENV = process.env.ENV?process.env.ENV:"test";
//console.log("Using Environment "+ENV)
const BASE_ROUTE = "";

export async function getUPIQR(data) {
  let res = new Response();
  let route = "/upi-qr?";
  res = await fetch(
    route +
      new URLSearchParams({
        adr: data.upi_adr,
        name: data.name,
        amount: data.amount,
      }).toString()
  );
  return res;
}
