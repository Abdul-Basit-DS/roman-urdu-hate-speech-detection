function processText() {
    let comment = document.getElementById("comment").value.trim();
    if (comment === "") {
        alert("Please enter a comment!");
        return;
    }

    console.log("🚀 Sending comment:", comment);

    document.getElementById("loading").style.display = "block";  

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ comment: comment }),
    })
    .then(response => response.json())
.then(result => {
    console.log("✅ Received result:", result);
    document.getElementById("loading").style.display = "none";
    document.getElementById("resultCard").style.display = "block";
    document.getElementById("dt_result").innerText = result["decision_tree"];
    document.getElementById("rf_result").innerText = result["random_forest"];
    document.getElementById("nb_result").innerText = result["naive_bayes"];
})

    .catch(error => {
        console.error("❌ Fetch error:", error);
        document.getElementById("loading").style.display = "none";
        alert("Error: " + error);
    });
}
