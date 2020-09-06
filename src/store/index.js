import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videosData:[],
  },
  mutations: {
    setVideoData(state, data){
      state.videosData = [data]
    },
    setVideoList(state, data){
      state.videosData = data;
    }
  },
  actions: {
  },
  modules: {
  },
  getters: {
    getVideo: state => {
      return state.videosData
    }
  }
})
