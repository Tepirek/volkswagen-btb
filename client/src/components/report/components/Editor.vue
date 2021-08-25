<template>
  <v-layout column align-center justify-center fill-height>
    <v-card
      class="d-flex flex-column fill-height"
      width="100%"
    >
      <v-flex shrink>
       <v-card-title>
         {{ componentType.name }}
         <v-spacer></v-spacer>
         <tooltip-left
           icon="mdi-rotate-3d-variant"
           :text= "$t('report.edit_dialog.flip_element')"
           @click="swapImage"
           :show="!singleSided"
         >
         </tooltip-left>
      </v-card-title>
      </v-flex>
      <v-flex shrink>
        <custom-divider></custom-divider>
      </v-flex>
      <v-flex grow>
        <v-card-text class="d-flex fill-height align-center justify-center">
          <div class="imageWrapper">
            <div class="imageWrapperPoints">
              <img
                @dragstart="e => e.preventDefault()"
                class="cardImage"
                :src="componentType.image"
                @click="addError" />
            </div>
          </div>
        </v-card-text>
      </v-flex>
      <v-flex shrink>
        <custom-divider></custom-divider>
      </v-flex>
      <v-flex shrink>
        <v-card-actions class="d-flex">
          <v-layout row class="pa-3">
            <v-flex class="xs4 pa-2 my-auto">
              <v-layout row align-center justify-center>
                <v-icon
                  color="black"
                  class="mr-3"
                  @click="updateErrorDialogVisible(true)"
                >
                  mdi-bug
                </v-icon>
                <v-icon
                  color="black"
                  class="mr-3"
                  @click="editMode = !editMode"
                >
                  {{ editModeIcon }}
                </v-icon>
                <img
                @dragstart="e => e.preventDefault()"
                v-if="!!errorPreviewImage"
                class="errorPreview"
                :src="errorPreviewImage" />
              </v-layout>
            </v-flex>
            <v-flex class="xs3 sm4 pa-2 my-auto">
              <v-layout row align-center justify-center>
                <v-icon
                  color="black"
                  @click="swapElement(-1)"
                >
                  mdi-arrow-left
                </v-icon>
                <v-icon
                  color="black"
                  class="ml-2 mr-2"
                >
                  mdi-dots-grid
                </v-icon>
                <v-icon
                  color="black"
                  @click="swapElement(1)"
                >
                  mdi-arrow-right
                </v-icon>
              </v-layout>
            </v-flex>
            <v-flex class="xs5 sm4 pa-2 my-auto">
              <v-layout row align-center justify-end>
                <v-btn
                  v-if="step > 1"
                  class="d-flex d-none"
                  small
                  text
                  @click="updateStep(step - 1)"
                >
                 {{ $t('report.edit_dialog.buttons.go_back_button') }}
                </v-btn>
                <v-btn
                  v-if="step <= 5"
                  small
                  color="primary"
                  @click="updateStep(step + 1)"
                >
                  {{ $t('report.edit_dialog.buttons.go_next_button') }}
                </v-btn>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-card-actions>
      </v-flex>
    </v-card>
    <bug-dialog
      @clickAction="editMode = true"
    ></bug-dialog>
    <point-delete-confirm-dialog
      v-model="deleteConfirmVisible"
      :data="point"
      @close="deleteConfirmVisible = false"
      @confirm="deletePointAction"
    ></point-delete-confirm-dialog>
  </v-layout>
</template>
<script>
import TooltipLeft from '@/components/reusable/TooltipLeft'
import CustomDivider from '@/components/reusable/CustomDivider'
import { mapActions, mapState } from 'vuex'
import BugDialog from '@/components/report/components/BugDialog'
import PointDeleteConfirmDialog from '../../reusable/PointDeleteConfirmDialog'

export default {
  name: 'Editor',
  components: { PointDeleteConfirmDialog, BugDialog, CustomDivider, TooltipLeft },
  data () {
    return {
      editMode: false,
      deleteConfirmVisible: false
    }
  },
  computed: {
    ...mapState('report/report', {
      report: state => state.report
    }),
    ...mapState('componentType', {
      componentTypeInit: state => state.isInit,
      componentTypes: state => state.componentTypes,
      componentType: state => state.componentType
    }),
    ...mapState('errorType', {
      errorTypes: state => state.errorTypes,
      errorType: state => state.errorType
    }),
    ...mapState('inclusionType', {
      inclusionTypes: state => state.inclusionTypes,
      inclusionType: state => state.inclusionType
    }),
    ...mapState('point', {
      points: state => state.points,
      point: state => state.point
    }),
    ...mapState('stepper', {
      step: state => state.step
    }),
    singleSided () {
      return this.componentTypeInit ? this.componentTypes[`${this.componentType.name}`].length === 1 : true
    },
    errorPreviewImage () {
      return this.inclusionType ? this.inclusionType.marker : this.errorType ? this.errorType.marker : null
    },
    editModeIcon () {
      return this.editMode ? 'mdi-pen' : 'mdi-pen-off'
    }
  },
  methods: {
    ...mapActions('point', {
      fetchAllPoints: 'fetchAll',
      createPoint: 'create',
      deletePoint: 'delete',
      updatePoint: 'updatePoint',
      removePoint: 'removePoint'
    }),
    ...mapActions('componentType', {
      fetchAllComponentTypes: 'fetchAll',
      updateComponentType: 'updateComponentType',
      toggleComponentType: 'toggleComponentType'
    }),
    ...mapActions('stepper', {
      updateStep: 'updateStep',
      updateErrorDialogVisible: 'updateErrorDialogVisible'
    }),
    ...mapActions('editDialog', {
      toggleErrorDialog: 'toggleDisplayVisible'
    }),
    swapImage () {
      this.toggleComponentType()
      this.displayPoints()
    },
    swapElement (direction) {
      this.updateComponentType(direction)
      this.displayPoints()
    },
    deletePointAction (point) {
      this.deletePoint(point.id)
        .then(_ => {
          this.deleteConfirmVisible = false
          point.imageElement.parentElement.removeChild(point.imageElement)
          this.removePoint(point.id)
        })
    },
    getMarker (data, id) {
      let marker = null
      data.some(e => {
        if (e.id === id) {
          marker = e.marker
        }
      })
      return marker
    },
    getErrorImage (point) {
      const errorTypeId = point.error_type ? point.error_type.id : null
      const inclusionTypeId = point.inclusion_type ? point.inclusion_type.id : null
      const errorTypeMarker = this.getMarker(this.errorTypes, errorTypeId)
      const inclusionTypeMarker = this.getMarker(this.inclusionTypes, inclusionTypeId)
      return inclusionTypeMarker || (errorTypeMarker || null)
    },
    addError (e) {
      if (!this.editMode) return
      const source = e.target
      var x = (e.layerX - 5) * 100 / source.clientWidth
      var y = (e.layerY - 5) * 100 / source.clientHeight
      this.createPoint({
        x: x,
        y: y,
        error_type: this.errorType ? this.errorType.id : null,
        inclusion_type: this.inclusionType ? this.inclusionType.id : null,
        component_type: this.componentType ? this.componentType.id : null,
        stage: this.step,
        report: this.report ? this.report.id : null
      })
        .then(_ => {
          this.displayPoints()
        })
    },
    displayPoints () {
      const parent = document.querySelector('.imageWrapperPoints')
      Array.from(this.points).forEach(point => {
        if (point.component_type.id === this.componentType.id) {
          if (!point.imageElement) {
            const pointElement = document.createElement('img')
            pointElement.style = `
              position: absolute;
              top: ${point.y}%;
              left: ${point.x}%;
              width: 10px;
              height: 10px;
              z-index: 5;
              display: block;
            `
            pointElement.src = this.getErrorImage(point)
            pointElement.addEventListener('click', () => {
              if (this.editMode) return
              this.updatePoint(point)
              this.deleteConfirmVisible = true
            })
            pointElement.addEventListener('dragstart', e => e.preventDefault())
            parent.appendChild(pointElement)
            point.imageElement = pointElement
          } else {
            point.imageElement.style.display = 'block'
          }
        } else if (point.imageElement) {
          point.imageElement.style.display = 'none'
        }
      })
    }
  },
  watch: {
    report: {
      handler (nv) {
        if (nv && nv.body_type) {
          this.fetchAllComponentTypes({ body_type: nv.body_type.id })
        }
      },
      immediate: true
    },
    componentTypeInit: {
      handler (nv) {
        if (nv) {
          this.fetchAllPoints({ report: this.report.id })
            .then(_ => {
              this.displayPoints()
            })
        }
      },
      immediate: true
    }
  }
}
</script>
<style scoped>
  .imageWrapper {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  }
  .imageWrapperPoints {
    position: relative;
  }
  .cardImage {
    width: 100%;
    max-height: calc(100vh - 324px);
    object-fit: contain;
  }
  .errorPreview {
    width: 24px;
    height: 24px;
    background-color: black;
  }
</style>
