function filterTable() {
    var input = document.getElementById('searchInput');
    var filter = input.value.toLowerCase();
    var table = document.getElementById('inventoryTable');
    var rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var name = rows[i].getElementsByTagName('td')[1];
        var sku = rows[i].getElementsByTagName('td')[2];
        var supplier = rows[i].getElementsByTagName('td')[5];

        if (name && sku && supplier) {
            var nameText = name.textContent || name.innerText;
            var skuText = sku.textContent || sku.innerText;
            var supplierText = supplier.textContent || supplier.innerText;

            if (nameText.toLowerCase().indexOf(filter) > -1 ||
                skuText.toLowerCase().indexOf(filter) > -1 ||
                supplierText.toLowerCase().indexOf(filter) > -1) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    }
}
