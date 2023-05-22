const form = document.getElementById("form");
const report = document.getElementById("generate-report");

const sendData = (data) => {
  fetch("<api URL>", {
    method: "POST",
    type: "application/json"
  })
    .catch((err) => console.log(err));
}

const generateReport = (transaction) => {
  let report;

  fetch("<api URL>", {
    method: "GET",
    type: "application/json"
  })
    .then((data) => {
      report = JSON.parse(data);
    })
    .catch((err) => console.log(err))

  return report;
}

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const from = document.getElementById("from");
  const to = document.getElementById("to");
  const value = document.getElementById("value");

  const transaction = {
    "type": "transaction",
    "from": from.value,
    "to": to.value,
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
    "from": from.value,
    "to": to.value
  }

  generateReport(transaction);
})

