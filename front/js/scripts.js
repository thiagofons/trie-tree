const form = document.getElementById("form");
const report = document.getElementById("generate-report");

const sendData = (data) => {
  fetch("http://localhost:5000/transaction", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .catch((err) => console.log(err));
}

const generateReport = async (transaction) => {

  await fetch("http://localhost:5000/report", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(transaction)
  })
    .then((data) => {
      return JSON.parse(data);
    })
    .catch((err) => console.log(err))
}

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const from = document.getElementById("from");
  const to = document.getElementById("to");
  const value = document.getElementById("value");

  const transaction = {
    "type": "transaction",
    "sender": from.value,
    "receiver": to.value,
    "value": value.value
  }

  // send data to back-end
  sendData(transaction);

  from.value = null;
  to.value = null;
  value.value = null;
});

report.addEventListener("click", (e) => {
  e.preventDefault();

  const from = document.getElementById("from");
  const to = document.getElementById("to");

  const transaction = {
    "type": "report",
    "sender": from.value,
    "receiver": to.value
  }
  
  const reportAPI = generateReport(transaction);
  console.log(reportAPI);
})

