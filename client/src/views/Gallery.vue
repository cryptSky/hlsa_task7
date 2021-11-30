<template>
  <div>
    <gallery :images="images" :index="index" @close="index = null"></gallery>
    <div
      class="image"
      v-for="(image, imageIndex) in images"
      :key="imageIndex"
      v-on:click.self="index = imageIndex"
      :style="{ backgroundImage: 'url(' + image + ')', width: '300px', height: '200px' }"
    >
    <span></span>
    <button @click="invalidateCache(imageIndex)">{{cache_stat[imageIndex]}}</button>
    </div>
  </div>
</template>

<script>
  import VueGallery from 'vue-gallery';
  import md5 from 'md5';
  
  export default {
    data: function () {
      return {
        cache_stat: Array(13).fill("Invalidate cache"),
        images: [
          'http://localhost:1337/gallery/0.jpg',
          'http://localhost:1337/gallery/1.jpg',
          'http://localhost:1337/gallery/2.jpg',
          'http://localhost:1337/gallery/3.jpg',
          'http://localhost:1337/gallery/4.jpg',
          'http://localhost:1337/gallery/5.jpg',
          'http://localhost:1337/gallery/6.jpg',
          'http://localhost:1337/gallery/7.jpg',
          'http://localhost:1337/gallery/8.jpg',
          'http://localhost:1337/gallery/9.jpg',
          'http://localhost:1337/gallery/10.jpg',
          'http://localhost:1337/gallery/11.jpg',
          'http://localhost:1337/gallery/12.jpg'
        ],
        index: null
      };
    },
    methods: {
      invalidateCache(index) {
          console.log(index)

          let url = new URL(this.images[index])
          console.log(url.pathname)
          let param = md5(url.pathname)

          return fetch('http://localhost:1337/gallery/'+param, {
              method: 'DELETE'
          }).then(response => {
              if (response.ok) {
                this.$set(this.cache_stat, index, "Cache invalidated")
                //this.cache_stat[index] = "Cache invalidated"
                console.log(response)
              }

            });
        }
    },

    components: {
      'gallery': VueGallery
    },
  }
</script> 

<style scoped>
  .image {
    float: left;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    border: 1px solid #ebebeb;
    margin: 5px;
  }
</style>

