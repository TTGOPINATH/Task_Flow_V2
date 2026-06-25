async function downloadProjectReport() {

    try {

        const response =
        await fetch(
            "/reports/projects"
        );

        if (!response.ok) {

            throw new Error(
                "Failed to generate report"
            );
        }

        const blob =
        await response.blob();

        const url =
        window.URL.createObjectURL(
            blob
        );

        const link =
        document.createElement(
            "a"
        );

        link.href = url;

        link.download =
        "projects_report.pdf";

        document.body.appendChild(
            link
        );

        link.click();

        link.remove();

        window.URL.revokeObjectURL(
            url
        );

    }

    catch(error) {

        console.error(error);

        alert(
            "Unable to download report"
        );
    }
}

document
.addEventListener(
    "DOMContentLoaded",

    function() {

        const btn =
        document.getElementById(
            "downloadReportBtn"
        );

        if(btn){

            btn.addEventListener(
                "click",
                downloadProjectReport
            );
        }
    }
);