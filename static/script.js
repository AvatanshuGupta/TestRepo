document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const questions = document.querySelectorAll(".question");
    const submitBtn = document.querySelector("button");

    // Optional: live answer counter
    const counter = document.createElement("p");
    counter.id = "counter";
    counter.textContent = `Answered 0 of ${questions.length}`;
    form.insertBefore(counter, submitBtn);

    questions.forEach((q, index) => {
        const radios = q.querySelectorAll("input[type='radio']");
        radios.forEach(radio => {
            radio.addEventListener("change", () => {
                let answered = 0;
                questions.forEach(q2 => {
                    if (q2.querySelector("input[type='radio']:checked")) answered++;
                });
                counter.textContent = `Answered ${answered} of ${questions.length}`;
            });
        });
    });
});
