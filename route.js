import * as glide from "@glideapps/tables";

// Define the Glide API configuration
const assignmentsTable = glide.table({
    token: "33204157-b863-4efa-93ca-c1416b553f9c", // Your Glide API token
    app: "fgDX3GrKqcaik8yp89Wa", // Your Glide app ID
    table: "native-table-5Gvvu8MdADHtRG8aSV3H", // The Glide table name or ID
    columns: {
        distance: { type: "string", name: "enMsq" }, // Column for distance
        time: { type: "string", name: "xixyx" }, // Column for time
        routeUrl: { type: "string", name: "nOCqF" } // Column for route URL
    }
});

// Function to send data to Glide
async function sendDataToGlide(distance, time, routeURL) {
    const rowId = getUrlParameter('rowId'); // Get the row ID from the URL

    if (rowId) {
        try {
            // Update the Glide row with the new data
            await assignmentsTable.update(rowId, {
                data: {
                    distance: distance.toString(),
                    time: time.toString(),
                    routeUrl: routeURL
                }
            });

            console.log(`Successfully updated row: ${rowId}`);
        } catch (error) {
            console.error("Error updating row in Glide:", error);
        }
    } else {
        console.log("No Row ID found in URL.");
    }
}

// Function to get URL parameters (for retrieving rowId)
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name); // Return the value of the parameter
}
