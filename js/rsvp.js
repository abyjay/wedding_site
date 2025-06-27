const web_url = "https://script.google.com/macros/s/AKfycbwraf0U5j_TJJgH4wIDMxR7eR4DqRsWP5eO4y2Qlkv-JSZljtrGJFCBIWoxg3XfSwL0MA/exec";
console.log("RSVP JS Loaded");

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("rsvp-form");

  if (form) {
    form.addEventListener("submit", function(e) {
      e.preventDefault();

      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();

      console.log(name, email)

      if (name === "" || email === "") {
        alert("Please enter both your name and email.");
        return;
      }

    const urlEncoded = new URLSearchParams();
    urlEncoded.append('name', name);
    urlEncoded.append('email', email);
    console.log(urlEncoded)

    fetch(web_url, {
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    // body: urlEncoded.toString()
    body: JSON.stringify({
        name:name,
        email:email
    })
    })
      .then(res => res.text())
      .then(response => {
        alert("Thank you for your RSVP!");
        form.reset();
      })
      .catch(error => {
        console.error("Error!", error.message);
        alert("There was an error submitting your RSVP. Please try again.");
      });
    });
  }
});
