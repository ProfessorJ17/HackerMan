document.addEventListener('DOMContentLoaded', function() {
    const outputElement = document.getElementById('output');

    // Function to simulate typing with random delays
    function typeWithRandomDelay(text) {
        for (let char of text) {
            setTimeout(function() {
                outputElement.textContent += char;
                // Apply glitch effect randomly
                if (Math.random() < 0.1) {
                    outputElement.style.transform = 'rotate(' + (Math.random() * 10 - 5) + 'deg)';
                }
            }, Math.random() * 50); // Random delay between characters
        }
    }

    // Function to simulate executing commands slowly with random reversals
    function simulateCommands() {
        let lineNum = 0;
        setInterval(function() {
            lineNum++;
            if (lineNum >= commandText.length) {
                lineNum = 0;
                outputElement.textContent = ''; // Clear output after completion
            }
            const text = commandText[lineNum];
            if (lineNum % Math.floor(Math.random() * 4 + 2) === 0) { // Reverse every random line
                typeWithRandomDelay(reverseText(text));
            } else {
                typeWithRandomDelay(text); // Normal line
            }
        }, Math.random() * 3000 + 1000); // Random interval between lines
    }

    // Function to reverse text
    function reverseText(text) {
        return text.split('').reverse().join('');
    }

    // Run the simulation
    const commandText = [
        "sudo nmap -O <target IP>",
        // Add other command lines here...
    ];
    simulateCommands();
});
