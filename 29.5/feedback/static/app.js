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

// $('.delete').click(deleteTodo)

// async function deleteTodo() {
//     const id = $(this).data('id')
//     // alert(id)
//     await axios.delete(`/api/todos/${id}`)
//     // alert('deleted')
//     $(this).parent().remove()
// }