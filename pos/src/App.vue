<template>
  <div class="side-container">
    <div id="left">
      <HeaderInvoice username="udey" invoiceInfo="10.252.234.132" date="13/12/2022"></HeaderInvoice>
      <BodyInvoice :details="details"></BodyInvoice>
      <CommandsLeft :clearKabeh="clearKabeh"></CommandsLeft>
    </div>
    <div class="v1"></div>
    <div id="right">
      <Categories @filterCategory="filterCategory"></Categories>
      <Catalogues :products="filterCategory(selectedCategory)"  @addItem="handleAddItem"></Catalogues>
      <div class="v2"></div>
      <div id="admin-commands"></div>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import HeaderInvoice from './components/HeaderInvoice.vue'
import BodyInvoice from './components/BodyInvoice.vue'
import CommandsLeft from './components/CommandsLeft.vue'
import Categories from './components/Categories.vue'
import Catalogues from './components/Catalogues.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    HeaderInvoice,
    BodyInvoice,
    CommandsLeft,
    Categories,
    Catalogues
},
data(){
  return{
    discount: 0.05,
    details: [],
    products:[
      {
      name: "Paket Hemat McSpicy, Medium",
      price:"51000",
      category: 'Fast Food'
    },
    {
      name:"Paket Hemat Fish Fillet Burger, Medium",
      price:"43000",
      category: 'Fast Food'
    },
    {
      name: "Iced Coffee Latte",
      price: '21000',
      category: 'Beverages'
    },
    {
      name: "Iced Coffee Float",
      price: '22500',
      category: 'Beverages'
    },
    {
      name: 'Hot Coffee Sink',
      price: '88500',
      category: 'Beverages',
    },
    {
      name: 'Panas  French Fries Ayam Crispy',
      price: '62000',
      category: 'Pastry',
    },
    {
      name: 'Butter Croissant',
      price: '21000',
      category: 'Pastry'
    }
    ],
    category:[
      "Fast Food",
      "Pastry",
      "Beverages"
    ],
    selectedCategory: "kabeh"
  }
},
methods: {

  handleAddItem(productObj) {
    console.log(`trying to add ${productObj.name}`)
    let namanamayangpernahada = this.details.map(barangyangada => barangyangada.name)
    let namanamayangpernahadaunique = [...new Set(namanamayangpernahada)];
    let iniperlunambahorangbaru = namanamayangpernahadaunique.indexOf(productObj.name) > -1

    if (!iniperlunambahorangbaru){
      this.details.push({
        name : productObj.name,
        qty : 1 ,
        price : productObj.price
      })
      
    } else {
      let indexdarinamaorangitu = this.details.findIndex((obj => obj.name == productObj.name))
      console.log("Index Orang")
      console.log(indexdarinamaorangitu)
      this.details[indexdarinamaorangitu].qty += 1
      
    }    
  },

  clearKabeh(){
    this.details = []
  },

  filterCategory(category){
    this.selectedCategory = category
    if (category == 'kabeh'){
      return this.products
    } else{
      return this.products.filter(e => e.category == category)
    }
  },



}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.side-container {
  display: flex;
  width: 100%;
}
#left {
  width: 430px;
  height: 100vh;
}
#right {
  /* background-color: #2c3e50; */
  width: 100%;
  height: 100vh;
}
.profile {
  display: flex;
  gap: 5px
}
.user {
  display: flex;
  justify-content: space-between;
  padding: 15px;
}
.invoice-info{
  text-align: left;
  margin-top: 20px;
}
.v1{
  border-right: 1px solid black;
  height: 600px;
  margin-top: 30px;
}
.invoice-info td{
  padding-left:15px ;
}
.v2{
  border-bottom:1px solid rgb(119, 119, 119);
  width: 90%;
  margin-left: 30px;
}

</style>
