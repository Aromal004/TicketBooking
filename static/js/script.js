// Function to generate ticket
function generateTicket() {
    const name = document.getElementById('name').value;
    const branch = document.getElementById('branch').value;
    const phone = document.getElementById('phone').value;

    if (name && branch && phone) {
        document.getElementById('ticketName').innerText = `Name: ${name}`;
        document.getElementById('ticketBranch').innerText = `Branch: ${branch}`;
        document.getElementById('ticketPhone').innerText = `Phone: ${phone}`;
        document.getElementById('ticket').style.display = 'block';
        document.getElementById('downloadBtn').style.display = 'block';
        document.getElementById('ticketForm').submit();
    }
}

// Function to download ticket as PDF
function downloadTicket() {
    const ticketElement = document.getElementById('ticket');

    // Use html2canvas to capture the ticket element
    html2canvas(ticketElement).then(canvas => {
        const imgData = canvas.toDataURL('image/png'); // Convert canvas to image
        const pdf = new jsPDF('p', 'mm', 'a4'); // Create a new jsPDF instance

        const imgWidth = 190; // Set the width of the image
        const pageHeight = pdf.internal.pageSize.height; // Get the height of the PDF page
        const imgHeight = (canvas.height * imgWidth) / canvas.width; // Calculate the height of the image
        let heightLeft = imgHeight;

        let position = 0; // Position on the page to draw the image

        // If the image is larger than the page, split it into multiple pages
        if (heightLeft >= pageHeight) {
            while (heightLeft >= 0) {
                pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
                heightLeft -= pageHeight;
                position -= pageHeight; // Move down for the next page
                if (heightLeft >= 0) {
                    pdf.addPage(); // Add a new page if there’s more image left
                }
            }
        } else {
            pdf.addImage(imgData, 'PNG', 10, 0, imgWidth, imgHeight); // Add the image
        }

        pdf.save('movie_ticket.pdf'); // Save the PDF
    });
}
