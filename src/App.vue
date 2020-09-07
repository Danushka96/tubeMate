<template>
  <v-app>
    <v-app-bar
        app
        color="primary"
        dark
    >
      <div class="d-flex align-center">
        <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://i.ibb.co/SsNjKXM/Capture-removebg-preview.png"
            transition="scale-transition"
            width="160"
        />

<!--        <v-img-->
<!--            alt="Vuetify Name"-->
<!--            class="shrink mt-1 hidden-sm-and-down"-->
<!--            contain-->
<!--            min-width="100"-->
<!--            src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"-->
<!--            width="100"-->
<!--        />-->
      </div>

      <v-spacer></v-spacer>

      <v-btn
          href="https://github.com/danushka96/tubemate"
          target="_blank"
          text
      >
        <span class="mr-2">Latest</span>
        <v-icon>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <video-search-box/>
        <div v-if="getVideos() && getVideos().length !== 0">
          <video-data v-for="video in getVideos()" :key="video.display_id" :video=video class="my-4"></video-data>
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import VideoSearchBox from "@/components/VideoSearchBox";
import VideoData from "@/components/VideoData";

export default {
  name: 'App',
  components: {
    VideoData,
    VideoSearchBox,
  },
  data: () => ({}),
  methods: {
    getVideos() {
      // console.log(this.$store.state.videosData.length)
      return this.$store.state.videosData;
    }
  },
};
</script>
