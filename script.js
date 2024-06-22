document.getElementById("userDataForm").addEventListener("click", function(event) {
    
    var gender = document.getElementById("gender").value ;
    var age=document.getElementById("age").value;
    var icu_nicu=document.getElementById("icu_nicu").value;
    var admission=document.getElementById("admission").value;
    var insurance=document.getElementById("insurance").value;
    var religion=document.getElementById("religion").value;
    var ethnicity=document.getElementById("ethnicity").value;
    var marital_status=document.getElementById("marital_status").value;
    var blood=document.getElementById("blood").value;
    var circulatory=document.getElementById("circulatory").value;
    var congential=document.getElementById("congential").value;
    var digestive=document.getElementById("digestive").value;
    var endocrine=document.getElementById("endocrine").value;
    var genitourinary=document.getElementById("genitourinary").value;
    var infectious=document.getElementById("infectious").value;
    var injury=document.getElementById("injury").value;
    var mental=document.getElementById("mental").value;
    var muscular=document.getElementById("muscular").value;
    var misc=document.getElementById("misc").value;
    var neoplasms=document.getElementById("neoplasms").value;
    var nervous=document.getElementById("nervous").value;
    var pregnancy=document.getElementById("pregnancy").value;
    var prenatal=document.getElementById("prenatal").value;
    var respiratory=document.getElementById("respiratory").value;
    var skin=document.getElementById("skin").value;

    formData = {"gender": gender , "age":age,"icu_nicu":icu_nicu,"admission":admission,"insurance":insurance,"religion":religion,"ethnicity":ethnicity,"marital_status":marital_status,"blood":blood,"circulatory":circulatory,"congential":congential,"digestive":digestive,"endocrine":endocrine,"genitourinary":genitourinary,"infectious":infectious,"injury":injury,"mental":mental,"muscular":muscular,"misc":misc,"neoplasms":neoplasms,"nervous":nervous,"pregnancy":pregnancy,"prenatal":prenatal,"respiratory":respiratory,"skin":skin}

    console.log(formData);
    // Send form data to server using fetch
    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Assuming server responds with JSON
        }
        throw new Error("Network response was not ok.");
    })
    .then(data => {
        console.log("Server response:", data); // Handle server response
        // Optionally, display success message or perform actions based on response
        alert("Data submitted successfully!");
    })
    .catch(error => {
        console.error("There was a problem with the fetch operation:", error);
        // Handle errors (e.g., display error message)
        alert("An error occurred while submitting data. Please try again.");
    });
});