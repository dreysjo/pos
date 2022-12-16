<template>
  <div class="categories-section">
    <h3>CATEGORIES</h3>
    <div class="thecategories">
      <div class="fastFood" @click="filterCategoryVersiFileIni('Fast Food')" ><span class="material-symbols-outlined" >fastfood</span></div>
      <div class="pastry" @click="filterCategoryVersiFileIni('Pastry')"><span  class="material-symbols-outlined">bakery_dining</span></div>
      <div class="beverages" @click="filterCategoryVersiFileIni('Beverages')"><span class="material-symbols-outlined">local_cafe</span></div>
      <div class="reset" @click="filterCategoryVersiFileIni('kabeh')"><span class="material-symbols-outlined">widgets</span></div>
    </div>
  </div>

</template>

<script>

export default {
  name: 'Categories',
  props:[],
  methods: {
    filterCategoryVersiFileIni(category){
      return this.$emit('filterCategory', category)
    },
  },

  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.categories-section{
  text-align: left;
}
h3 {
  margin: 10px 20px;
  text-align: left;
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

.thecategories{
  display: flex;
  margin: 20px;
}

.thecategories{
  margin-top: 0px;
}
.thecategories span{
  margin: 0px 20px;
  padding: 20px;
}
span{
  background-color: blueviolet;
  border-radius:20px;
  text-align: left;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);
}

span:hover{
  background-color: #404040
}
.material-symbols-outlined{
  color: white;
}
</style>

