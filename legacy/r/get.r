# R API endpoint
#* @get /data
function() {
    return(data)
}

# JavaScript
fetch('/data')
    .then(response => response.json())
    .then(data => console.log(data))
