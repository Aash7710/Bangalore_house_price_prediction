// Fetch the selected bathroom value
function getBathValue() {
    var uiBathrooms = document.getElementById("uiBathrooms");
    return parseInt(uiBathrooms.value); // Get the value of the selected bathroom option
}

// Fetch the selected balcony value
function getBalconyValue() {
    var uiBalcony = document.getElementById("uiBalcony");
    return parseInt(uiBalcony.value); // Get the value of the selected balcony option
}


  // Fetch the selected BHK value
  function getBHKValue() {
    var uiBHK = document.getElementById("uiBHK");
    return parseInt(uiBHK.value); // Get the value of the selected BHK option
}

  // Handle the price estimation when the button is clicked
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var balcony = getBalconyValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    // Ensure the URL is correct
    var url = "http://127.0.0.1:5000/predict_home_price"; // Adjust the URL if needed

    $.post(url, {
      total_sqft: parseFloat(sqft),
      bhk: bhk,
      bath: bathrooms,
      balcony: balcony,
      location: location
    }, function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>"; // Display the estimated price
      console.log(status);
    });
  }

  // Load location data on page load
  function onPageLoad() {
    console.log("Document loaded");

    // Ensure the URL is correct
    var url = "http://127.0.0.1:5000/get_location_names"; // Adjust the URL if needed

    $.get(url, function(data, status) {
      console.log("Got response for get_location_names request");
      if (data) {
        var locations = data.locations;
        var uiLocations = document.getElementById("uiLocations");
        $('#uiLocations').empty(); // Clear any existing options
        for (let location of locations) {
          var opt = new Option(location); // Create new option for each location
          $('#uiLocations').append(opt); // Append the option to the select element
        }
      }
    });
  }

  // Ensure onPageLoad runs when the window loads
  window.onload = onPageLoad;
