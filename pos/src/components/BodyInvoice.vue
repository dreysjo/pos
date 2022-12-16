<template>
  <h3>DETAIL</h3>
  <div class="table-section">
      <table  class="table">
      <thead>
        <tr>
          <th scope="col">ITEM</th>
          <th scope="col">QTY</th>
          <th scope="col">PRICE</th>
          <th scope="col">TOTAL</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in details">
          <td>{{ item.name }}</td>
          <td>{{ item.qty }}</td>
          <td>Rp.{{ item.price }}</td>
          <td>Rp.{{ item.price * item.qty }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="totals">
    <table>
      <tr>
        <td>Total</td>
        <td>Rp. {{sumTotal}}</td>
      </tr>
      <tr>
        <td>Discount</td>
        <td>{{discount * 100}}%</td>
      </tr>
      <tr>
        <td>Grand Total</td>
        <td>Rp. {{getGrandTotal}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import { computed } from 'vue';

export default {
  name: 'BodyInvoice',
  props: ['details'],
  
  data()  {
  return {
    discount: 0.05,
  }},
  computed: {
    sumTotal() {
      let total = 0
      for (let i in this.details) {
        console.log(i)
        total+= this.details[i].qty * this.details[i].price
      }
      return total
    },
    getGrandTotal(){
      return this.sumTotal * (1-this.discount)
    },
  },

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3 {
  display: flex;
  padding-left: 15px;
  margin: 30px 0 0;
  align-items: flex-start;
  font-weight: 500px;
}
.table-section{
  border-radius: 20px;
  margin: 10px;
  padding: 0px;
  background: #F1F1F1;
}
.table-section td,th {
  font-size: 12px;
  line-height: 8px;
}
.table-section {
  
  max-height: 40vh;
  padding: 12px;
  overflow-y:scroll;
}
.table-section::-webkit-scrollbar {
  display: none;
}
.totals {
  display: flex;
  justify-content: flex-end;
  padding-right: 25px;
  padding-top: 10px;
}
.totals td,th{
  padding-left: 20px;
  line-height: 20px;
  text-align: left;
  font-size: 15px;
}

table thead tr,th{
  padding-right: 25px;
}
</style>
