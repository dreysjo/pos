<template>
  <div class="catalogue-section">
    <div v-for="(product,index) in products">
      <div class="gallery">
      <span>{{product.name}}</span>
      <p class="price">Rp.{{product.price}}</p>
      <button type="submit" class="butt" @click="getItem(index)">add</button>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Catalogues',
  props: ['products'],
  component: {
    msg:String
  },
  data(){
    return{
     }
  },
  methods:{
    // getIndex(index){
    //   // this.selectedIndex = index
    //   // console.log(this.selectedIndex)
    //   // return this.selectedIndex
    //   this.$emit('add-item, ')
    // },
    // sendToRoot(name) {
    //   this.$emit('add-item', name)
    // },
    getItem(index){
      console.log("HELLO")
      this.selectedIndex = index
      let productObj = this.products[this.selectedIndex]
      this.$emit('addItem', productObj)
    },
  },
  computed:{
    getSelectedIndex(){
      return this.getIndex(index)
    }
  },
  emits: ['addItem']

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
p{
  /* position: absolute; */
  color: white;
  padding-top: 5px;
  margin-top: 10px;
  /* padding: 60px 65px; */
  font-weight: 300;
}
a {
  color: #42b983;
}
.catalogue-section {
  max-height: 60vh;
  /* border-bottom: 0.5px solid grey; */
  padding: 12px;
  overflow-y:scroll;
}
/* .catalogue-section::-webkit-scrollbar {
  display: none;
} */
.gallery{
 background-color: rgb(85, 26, 124);
 margin: 20px 20px;
 float: left;
 width: 180px;
 height: 180px;
 border-radius: 20px;
 display: flex;
 flex-direction: column;

}

.gallery span{
  margin: auto;
  color: white;
}
.gallery .butt{
  border-radius: 20px;
  width: 35%;
  margin-left: 33%;
  margin-bottom: 20px;
  border: hidden;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);
  /* padding-top: 100px; */
}
.butt:hover{
  background-color: rgba(255, 43, 15, 0.747);
  color:white;
  border:hidden
}

</style>
