async function createGame() {
    // Call backend to create game
    console.log("createGame() called");
    const res = await fetch("/game/create", { method: "POST" });
    console.log("Response status:", res.status);
    const data = await res.json();
    console.log("Response data:", data);

    // Hide setup
    document.getElementById("setup-screen").style.display = "none";
}
