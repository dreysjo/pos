<template>
  <div id="header-invoice">
        <div class="user">
          <div class="profile">
            <div class="profile-pic"><i class="bi bi-person-circle"></i></div>
            <div class="profile-name">{{ username }}</div>
          </div>
          <div class="logout">
            <i class="bi bi-box-arrow-right"></i>
          </div>
        </div>
        <div class="invoice-info">
          <table>
            <tr>
              <td>Invoice</td>
              <td>{{invoiceInfo}}</td>
            </tr>
            <tr>
              <td>Date</td>
              <td>{{date}}</td>
            </tr>
          </table>
        </div>
      </div>
</template>

<script>
export default {
  name: 'HeaderInvoice',
  props: {
    username: String,
    invoiceInfo: String,
    date: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
