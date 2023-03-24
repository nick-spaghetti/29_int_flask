const base = "http://localhost:5000/api";
const toggleSwitch = document.querySelector('input[type="checkbox"]');
// const delete_btn = document.getElementsByClassName('delete');

if (localStorage.getItem('darkModeEnabled')) {
    document.body.className = 'dark';
    toggleSwitch.checked = true;
}

toggleSwitch.addEventListener('click', (e) => {
    const checked = toggleSwitch.checked;
    if (checked) {
        localStorage.setItem('darkModeEnabled', true);

    } else {
        localStorage.removeItem('darkModeEnabled');
    }
    document.body.className = checked ? 'dark' : "";
});

$('.delete').click(deleteCupcake)

async function deleteCupcake() {
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}


$("#new-cupcake-form").on("submit", async function (e) {
    e.preventDefault();

    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    const newCupcakeResponse = await axios.post(`${base}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });

    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
});

$("#update-cupcake-form").on("submit", async function (e) {
    e.preventDefault();
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let cupcakeId = $("#cupcake-id").val(); // assuming the id is stored in a hidden input field with id="cupcake-id"

    try {
        await axios.patch(`${base}/cupcakes/${cupcakeId}`, {
            flavor,
            rating,
            size
        });

        window.location.href = "index.html"; // redirect to the new page after the patch request is successful
    } catch (error) {
        console.log(error);
    }
});