<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Sales</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Invoice No</th>
              <th scope="col">Total</th>
              <th scope="col">Discount</th>
              <th scope="col">Grand Total</th>
              <th scope="col">Username</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sale, invoice_no) in sales" :key="invoice_no">
              <td>{{ sale.invoice_no }}</td>
              <td>{{ sale.total }}</td>
              <td>{{ sale.discount }}</td>
              <td>{{ sale.grand_total }}</td>
              <td>{{ sale.username }}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
    };
  },
  methods: {
    getSales() {
      const path = 'http://localhost:5000/get';
      axios.get(path)
        .then((res) => {
          this.sales = res.data.sales;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getSales();
  },
};
</script>