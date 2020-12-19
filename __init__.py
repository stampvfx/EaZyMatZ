bl_info = {
    "name" : "EaZyMatZ",
    "author" : "Youssef Hossam",
    "description" : "",
    "blender" : (2, 90, 1),
    "version" : (1, 0, 1), 
    "location" : "",
    "warning" : "",
    "category" : "Shading"
    }
import bpy
import os
class MainPanel(bpy.types.Panel):
    bl_label = "Basic Materials"
    bl_idname = "MainPanel_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EaZyMatZ"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('shader.wood_operator', text="Wood")
        row = layout.row()
        row.operator('shader.ocean_operator', text="Ocean")
        row = layout.row()
        row.operator('shader.car_operator', text="CarPaint")
        row = layout.row()
        row.operator('shader.asphalt1_operator', text="Asphalt Basic")
        row.operator('shader.asphaltadvanced_operator', text="Asphalt Advanced")
        row = layout.row()
        row.operator('shader.spongebasic_operator', text='Sponge Basic')
        row.operator('shader.advancedsponge_operator', text='Sponge Advanced')

        
        
        
class METALPANEL(bpy.types.Panel):
    bl_label = "Metals"
    bl_idname = "METALPANEL_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EaZyMatZ"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('shader.dentedmetal_operator', text='Dented Metal')
        row = layout.row()
        row.operator('shader.copp_operator', text='Copper')
        row.operator('shader.copp2_operator', text='Copper 2')
        row.operator('shader.copp3_operator', text='Copper 3')
        row = layout.row()
        row.operator('shader.brass_operator', text='Brass')
        row.operator('shader.brass2_operator', text='Brass 2')
        row = layout.row()
        row.operator('shader.ss_operator', text='Stainless Steel')
        row.operator('shader.ss2_operator', text='Stainless Steel 2')
        row = layout.row()
        row.operator('shader.chr_operator', text='Chrome')
        row = layout.row()
        row.operator('shader.darkmet_operator', text='Dark Metal')
        row = layout.row()
        row.operator('shader.alim_operator', text='Aluminium')
        row = layout.row()
        row.operator('shader.am_operator', text='AnodizedMetal')
        row = layout.row()
        row.operator('shader.kev_operator', text='Kevlar')
        row = layout.row()
        row.operator('shader.gm_operator', text='Ground metal')
 
 
 
 
 
class FABRICPANEL(bpy.types.Panel):
    bl_label = "Fabric"
    bl_idname = "FABRICPANEL_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EaZyMatZ"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('shader.satinfabric_operator', text='Fabric Satin')
        row.operator('shader.satinfabric2_operator', text='Fabric Satin 2')
        row = layout.row()
        row.operator('shader.upholstery_operator', text='Fabric UpHolstery')
        row.operator('shader.upholstery2_operator', text='Fabric UpHolstery 2')
        row.operator('shader.upholstery3_operator', text='Fabric UpHolstery 3')
        row = layout.row()
        row.operator('shader.silk_operator', text='Fabric Silk')
        row.operator('shader.silk2_operator', text='Fabric Silk 2')
        row = layout.row()
        row.operator('shader.crushed_operator', text='Crushed Fabric')
        row.operator('shader.crushed2_operator', text='Crushed Fabric 2')
        row = layout.row()
        row.operator('shader.leather_operator', text='Fabric Leather')
        row = layout.row()
        row.operator('shader.felt_operator', text='Fabric Felt')
        row = layout.row()
        row.operator('shader.st_operator', text='Fabric Semi Transparent')
        row = layout.row()
        row.operator('shader.leth2_operator', text='Fabric Leather 2')
    
 

 

     
        

     
        
        

#WoodShaderOperator
class MATZOTWOOD(bpy.types.Operator):
    bl_label = "Assign Wood Material"
    bl_idname = 'shader.wood_operator'
    def execute(self, context):
        #CreateWoodShader
        material_wood = bpy.data.materials.new(name = "Wood")
        material_wood.use_nodes = True

        material_output = material_wood.node_tree.nodes.get('Material Output')
        
        
        #princibledbsdf
        BSDF = material_wood.node_tree.nodes.get('Principled BSDF')

        #definelocation
        material_output.location = (2.3,0)

        #ColorRampNode
        colorramp_node = material_wood.node_tree.nodes.new('ShaderNodeValToRGB')


        #definelocaton
        colorramp_node.location = (200, 6)
       
        colorramp_node.color_ramp.elements[0].color = (0.141263, 0.0865005, 0.0395462, 1)
        colorramp_node.color_ramp.elements[1].color = (0.274677, 0.171441, 0.0722719, 1)


        #NoiseTexNode
        noisetex_node = material_wood.node_tree.nodes.new('ShaderNodeTexNoise')

        #definelocation
        noisetex_node.location = (-200, 6)
        
        noisetex_node.inputs[4].default_value = 0.766667

        #definesettings

        noisetex_node.inputs[2].default_value = 1
        noisetex_node.inputs[3].default_value = 16
        noisetex_node.inputs[5].default_value = 1



        #MappingNode
        mapping_node = material_wood.node_tree.nodes.new('ShaderNodeMapping')

        #definelocation
        mapping_node.location = (-20, 8)

        #definesettings
        mapping_node.inputs[3].default_value[1] = 6.45

        #TexCoord
        texcoord_node = material_wood.node_tree.nodes.new('ShaderNodeTexCoord')

        #definelocation
        texcoord_node.location = (45, 5)
        
        
        #Bump
        bump_node = material_wood.node_tree.nodes.new('ShaderNodeBump')

        #definelocation
        bump_node.location = (90, 12)



        material_wood.node_tree.links.new(noisetex_node.outputs[0], colorramp_node.inputs[0])
        material_wood.node_tree.links.new(noisetex_node.outputs[1], bump_node.inputs[2])
        material_wood.node_tree.links.new(mapping_node.outputs[0], noisetex_node.inputs[0])
        material_wood.node_tree.links.new(texcoord_node.outputs[3], mapping_node.inputs[0])
        material_wood.node_tree.links.new(bump_node.outputs[0], BSDF.inputs[19])
        material_wood.node_tree.links.new(colorramp_node.outputs[0], BSDF.inputs[0])
        



        bpy.context.object.active_material = material_wood
        
        
        
        return {'FINISHED'}

        
        
        
        
        
#OceanShaderOperator
class MATZOTOCEAN(bpy.types.Operator):
    bl_label = "Assign Wood Material"
    bl_idname = 'shader.ocean_operator'
    def execute(self, context):
        #CreateOceanShader
        material_ocean = bpy.data.materials.new(name = "Ocean")
        material_ocean.use_nodes = True

        material_output = material_ocean.node_tree.nodes.get('Material Output')
        
        
        #princibledbsdf
        BSDF = material_ocean.node_tree.nodes.get('Principled BSDF')

        #definelocation
        material_output.location = (2.3,0)
        BSDF.location = (200,-90)
        
        
        
        BSDF.inputs[0].default_value = (0, 0.078871, 1, 1)
        BSDF.inputs[15].default_value = 1
        bpy.context.object.active_material = material_ocean
        
        return {'FINISHED'}
    
    
    
    
    
    
    
    
    
    #CarShaderOperator
class MATZOTCAR(bpy.types.Operator):
    bl_label = "Assign Wood Material"
    bl_idname = 'shader.car_operator'
    def execute(self, context):
        #CreateOceanShader
        material_car = bpy.data.materials.new(name = "CarMat")
        material_car.use_nodes = True

        material_output = material_car.node_tree.nodes.get('Material Output')
        
        
        #princibledbsdf
        BSDF = material_car.node_tree.nodes.get('Principled BSDF')

        #definelocation
        material_output.location = (2.3,0)
        BSDF.location = (200,-90)
        
        
        
        #colorrampnode
        
        colorrampcar_node = material_car.node_tree.nodes.new('ShaderNodeValToRGB')
        colorrampcar_node.color_ramp.elements[0].color = (1, 0.312009, 0.0291604, 1)
        colorrampcar_node.color_ramp.elements[1].color = (1, 0.117874, 0, 1)
        
        #layerweightnode 
        layerweightcar_node = material_car.node_tree.nodes.new('ShaderNodeLayerWeight')
        
        
        
        #lets link our nodes now :)
        
        material_car.node_tree.links.new(colorrampcar_node.outputs[0], BSDF.inputs[0])
        material_car.node_tree.links.new(layerweightcar_node.outputs[1], colorrampcar_node.inputs[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        bpy.context.object.active_material = material_car
        
        return {'FINISHED'}
    
    
    
    
    
    
     
    #Asphalt1ShaderOperator
class MATZOTASPHALT1(bpy.types.Operator):
    bl_label = "Assign Wood Material"
    bl_idname = 'shader.asphalt1_operator'
    def execute(self, context):
        #CreateAsphalt1Shader
        material_asphalt1 = bpy.data.materials.new(name = "Asphalt1Mat")
        material_asphalt1.use_nodes = True
        
        
        
        #materialoutput
        material_output = material_asphalt1.node_tree.nodes.get('Material Output')
        
        
        #princibledbsdf
        BSDF = material_asphalt1.node_tree.nodes.get('Principled BSDF')

        #definelocation
        material_output.location = (2.3,0)
        BSDF.location = (200,-90)
        
        
        #this is for the mixrgb input
        noiseasphalt1_node= material_asphalt1.node_tree.nodes.new('ShaderNodeTexNoise')
        noiseasphalt1_node.inputs[2].default_value = 10
        noiseasphalt1_node.inputs[3].default_value = 16
        
        
        
        #this is the only uvmapnode in this mat :)
        uvmapasphalt1_node = material_asphalt1.node_tree.nodes.new('ShaderNodeUVMap')
        
        
        #this mix is for nosietex1 and uv map
        mixrgbasphalt1_node = material_asphalt1.node_tree.nodes.new('ShaderNodeMixRGB')
        mixrgbasphalt1_node.inputs[0].default_value = 0.05
        
        
        
        #this is the second noise texture, which is for mixrgb1 output
        noiseasphalt2_node = material_asphalt1.node_tree.nodes.new('ShaderNodeTexNoise')
        noiseasphalt2_node.inputs[2].default_value = 50
        noiseasphalt2_node.inputs[3].default_value = 16
        
        
        
        #this is our first colorramp, which for noisetex2 output and mixrgb2 input we use this to make it black and white :)
        colorasphalt1_node = material_asphalt1.node_tree.nodes.new('ShaderNodeValToRGB')
        
        
        #this mix is our second one and which we will use to inout colorramp1 and output colorramp 2
        mixrgbasphalt2_node = material_asphalt1.node_tree.nodes.new('ShaderNodeMixRGB')
        
    
        
        
        
        #this the secone color ramp we will use this to input mixrgb2 and output colorramp3 ;)
        colorasphalt2_node = material_asphalt1.node_tree.nodes.new('ShaderNodeValToRGB')
        colorasphalt2_node.color_ramp.elements[0].position = 0.204545
        colorasphalt2_node.color_ramp.elements[1].position = 0.327273
        
        
        
        #this is the 3rd color ramp node which we will use to apply our colours
        colorasphalt3_node = material_asphalt1.node_tree.nodes.new('ShaderNodeValToRGB')
        colorasphalt3_node.color_ramp.elements[0].position = 0.15
        colorasphalt3_node.color_ramp.elements[0].position = 0.809091
        
        colorasphalt3_node.color_ramp.elements[0].color = (0.0802198, 0.114435, 0.168269, 1)
        colorasphalt3_node.color_ramp.elements[1].color = (0.0212635, 0.0266884, 0.0560386, 1)
       
    
        #this is our first and only voronoi texture in the whole mat :)s
        texvornasphalt1_node = material_asphalt1.node_tree.nodes.new('ShaderNodeTexVoronoi')
        
        
        texvornasphalt1_node.feature = 'DISTANCE_TO_EDGE'
        texvornasphalt1_node.inputs[2].default_value = 50
        
        
        
        #this is the fourth colorramp in our scene and the is the last one in our mat ;)
        colorasphalt4_node = material_asphalt1.node_tree.nodes.new('ShaderNodeValToRGB')
     
     
     
     
        #now let's create the only bump node in out material :)
        bumpasphalt1_node = material_asphalt1.node_tree.nodes.new('ShaderNodeBump')
        
        
        
        
        
        
        
        
        
        
        #now lets link our nodes
        
        
        link = material_asphalt1.node_tree.links.new
        
        link(noiseasphalt1_node.outputs[1], mixrgbasphalt1_node.inputs[2])
        link(uvmapasphalt1_node.outputs[0], mixrgbasphalt1_node.inputs[1])
        link(mixrgbasphalt1_node.outputs[0], noiseasphalt2_node.inputs[1])
        link(noiseasphalt2_node.outputs[1], colorasphalt1_node.inputs[0])
        link(colorasphalt1_node.outputs[0], mixrgbasphalt2_node.inputs[1])
        link(mixrgbasphalt2_node.outputs[0], colorasphalt2_node.inputs[0])
        link(colorasphalt2_node.outputs[0], colorasphalt3_node.inputs[0])
        link(colorasphalt3_node.outputs[0], BSDF.inputs[0])
        link(texvornasphalt1_node.outputs[0], mixrgbasphalt2_node.inputs[2])
        link(mixrgbasphalt2_node.outputs[0], colorasphalt4_node.inputs[0])
        link(colorasphalt4_node.outputs[0], bumpasphalt1_node.inputs[2])
        link(bumpasphalt1_node.outputs[0], BSDF.inputs[19])
             
        
        
        
     
        

        
      
       
        
     
        
        
        
        
        
      
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        bpy.context.object.active_material = material_asphalt1
        
        return {'FINISHED'}
        
        
        
        import os
        
        #now let's append advanced asphalt :)
        from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
        from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )


blend_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'materialasphaltadvanced', 'Asphalt.blend')


class MATZOTASPHALTADVANCED(bpy.types.Operator):
    bl_idname = 'shader.asphaltadvanced_operator'
    bl_label =  'Assign Asphalt Material'
    
    def execute(self, context):

        section = "\\Material\\"
                    
        objects = ["Asphalt"] 
        
        directory = blend_file + section
        
        for obj in objects:
            filename = obj
            bpy.ops.wm.append(filename=filename, directory=directory)
            
            
        
        
     
                        
        return{'FINISHED'}
    
    









sponge_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'materialspongebasic', 'spongebasicmat.blend')




class MATZOTSPONGEBASIC(bpy.types.Operator):
    bl_idname = 'shader.spongebasic_operator'
    bl_label =  'Assign Sponge Material'
    
    def execute(self, context):

        section = "\\Material\\"
                    
        objects = ["Sponge"] 
        
        directory = sponge_file + section
        
        for obj in objects:
            filename = obj
            bpy.ops.wm.append(filename=filename, directory=directory)

     
                        
        return{'FINISHED'}
    
dm_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals.blend')

   
    
class MATZOTDENTEDMETAL(bpy.types.Operator):
      bl_idname = 'shader.dentedmetal_operator'
      bl_label =  'Assign dentedmetal Material'
      
      def execute(self, context):

          section = "\\Material\\"
                    
          objects = ["Dented Metal"] 
        
          directory = dm_file + section
        
          for obj in objects:
              filename = obj
              bpy.ops.wm.append(filename=filename, directory=directory)
             
            
            
        
        
     
                        
          return{'FINISHED'}
      
      
      
      
      
      
      
      
      
      
      
      
      
      
fabricsla_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend')

   
    
class MATZOTFABRICSATIN(bpy.types.Operator):
      bl_idname = 'shader.satinfabric_operator'
      bl_label =  'Assign fabric satin Material'
      
      def execute(self, context):

          section = "\\Material\\"
                    
          objects = ["Fabric satin"] 
        
          directory = fabricsla_file + section
        
          for obj in objects:
              filename = obj
              bpy.ops.wm.append(filename=filename, directory=directory)
             
            
        
        
     
    
                        
          return{'FINISHED'}
    
    


fabricsla2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend')


class MATZOTFABRICSATIN2(bpy.types.Operator):
      bl_idname = 'shader.satinfabric2_operator'
      bl_label =  'Assign fabric satin2 Material'
      
      def execute(self, context):

          section = "\\Material\\"
                    
          objects = ["Fabric Satin 2"] 
        
          directory = fabricsla2_file + section
        
          for obj in objects:
              filename = obj
              bpy.ops.wm.append(filename=filename, directory=directory)
       
        
        
     
                        
          return{'FINISHED'}
      
      
      
fabricuphol_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend')   
class MATZOTFABRICUPHOLSTERY(bpy.types.Operator):
       bl_idname = 'shader.upholstery_operator'
       bl_label =  'Assign fabric upholstery Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Fabric UpHolstery"] 
        
           directory = fabricsla2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)

                        
           return{'FINISHED'}
    
    


    
        
fabricuphol2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend')   
class MATZOTFABRICUPHOLSTERY2(bpy.types.Operator):
       bl_idname = 'shader.upholstery2_operator'
       bl_label =  'Assign fabric upholstery2 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Fabric UpHolstery 2"] 
        
           directory = fabricsla2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
        
     
    
                        
           return{'FINISHED'}
       
       
       
       
       
fabricuphol3_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend')   
class MATZOTFABRICUPHOLSTERY3(bpy.types.Operator):
       bl_idname = 'shader.upholstery3_operator'
       bl_label =  'Assign fabric upholstery3 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Fabric UpHolstery 3"] 
        
           directory = fabricsla2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory) 
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
fabricsilk_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend') 
class MATZOTFABRICSILK(bpy.types.Operator):
       bl_idname = 'shader.silk_operator'
       bl_label =  'Assign fabric silk Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["fabric silk"] 
        
           directory = fabricsilk_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)

     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
fabricsilk2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend') 
class MATZOTFABRICSILK2(bpy.types.Operator):
       bl_idname = 'shader.silk2_operator'
       bl_label =  'Assign fabric silk2 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["fabric silk 2"] 
        
           directory = fabricsilk2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
         
        
        
     
                        
           return{'FINISHED'}
       
       
       
fabriccrushed_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend') 
class MATZOTFABRICCRUSHED(bpy.types.Operator):
       bl_idname = 'shader.crushed_operator'
       bl_label =  'Assign fabric crushed Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Fabric Crushed"] 
        
           directory = fabriccrushed_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
       
        
     
                        
           return{'FINISHED'}
       
       
       
    
fabriccrushed2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend') 
class MATZOTFABRICCRUSHED2(bpy.types.Operator):
       bl_idname = 'shader.crushed2_operator'
       bl_label =  'Assign fabric crushed Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Fabric Crushed 2"] 
        
           directory = fabriccrushed2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
fabricleather_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'leather.blend') 
class MATZOTFABRICLEATHER(bpy.types.Operator):
       bl_idname = 'shader.leather_operator'
       bl_label =  'Assign fabric leather Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Leather"] 
        
           directory = fabricleather_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
          
        
          
                        
           return{'FINISHED'}
    
    


    
fabricfelt_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend') 
class MATZOTFABRICFELT(bpy.types.Operator):
       bl_idname = 'shader.felt_operator'
       bl_label =  'Assign fabric felt Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["fabric felt"] 
        
           directory = fabricfelt_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
          
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
fabricst_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'fabric library.blend') 
class MATZOTFABRICST(bpy.types.Operator):
       bl_idname = 'shader.st_operator'
       bl_label =  'Assign fabric semi transparent Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["fabric semi transparent"] 
        
           directory = fabricst_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
       
       
copp_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTCOPPER(bpy.types.Operator):
       bl_idname = 'shader.copp_operator'
       bl_label =  'Assign copper Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Copper"] 
        
           directory = copp_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
       
       
       
copp2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTCOPPER2(bpy.types.Operator):
       bl_idname = 'shader.copp2_operator'
       bl_label =  'Assign copper2 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Copper 2"] 
        
           directory = copp2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
copp3_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTCOPPER3(bpy.types.Operator):
       bl_idname = 'shader.copp3_operator'
       bl_label =  'Assign copper3 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Copper 3"] 
        
           directory = copp3_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
       
    
    
    
    
    
brass_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTBRASS(bpy.types.Operator):
       bl_idname = 'shader.brass_operator'
       bl_label =  'Assign brass Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Brass 1"] 
        
           directory = brass_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
brass2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTBRASS2(bpy.types.Operator):
       bl_idname = 'shader.brass2_operator'
       bl_label =  'Assign brass Material'
      
       def execute(self, context):

           section = "\\Material\\"
                    
           objects = ["Brass 2"] 
        
           directory = brass2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
    
    
    
    
    
    
ss_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTSS(bpy.types.Operator):
       bl_idname = 'shader.ss_operator'
       bl_label =  'Assign ss Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["StainlessSteel"] 
        
           directory = ss_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
       
ss2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTSS2(bpy.types.Operator):
       bl_idname = 'shader.ss2_operator'
       bl_label =  'Assign ss2 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["StainlessSteel2"] 
        
           directory = ss2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
chrome_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTCHROME(bpy.types.Operator):
       bl_idname = 'shader.chr_operator'
       bl_label =  'Assign chr Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["Chrome"] 
        
           directory = chrome_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
darkmet_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTDARKMET(bpy.types.Operator):
       bl_idname = 'shader.darkmet_operator'
       bl_label =  'Assign darkmet Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["DarkMetal"] 
        
           directory = darkmet_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
alim_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTALIMINUIM(bpy.types.Operator):
       bl_idname = 'shader.alim_operator'
       bl_label =  'Assign alim Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["Aluminium"] 
        
           directory = alim_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
       
       
       
am_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTAM(bpy.types.Operator):
       bl_idname = 'shader.am_operator'
       bl_label =  'Assign am Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["AnodizedMetal"] 
        
           directory = am_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
kevlar_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'metals12.blend') 
class MATZOTKEV(bpy.types.Operator):
       bl_idname = 'shader.kev_operator'
       bl_label =  'Assign kev Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["Kevlar"] 
        
           directory = kevlar_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
       
       
       
       
leth2_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Fabric', 'leath.blend') 
class MATZOTLEATH(bpy.types.Operator):
       bl_idname = 'shader.leth2_operator'
       bl_label =  'Assign leth2 Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["leather 2"] 
        
           directory = leth2_file + section
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}






groundmetal_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'allmetals', 'groundmetal.blend') 
class MATZOTGM(bpy.types.Operator):
       bl_idname = 'shader.gm_operator'
       bl_label =  'Assign Ground metal Material'
      
       def execute(self, context):

           section = "\\Material\\"
                
           objects = ["Ground metal"] 
        
           directory = groundmetal_file + section 
        
           for obj in objects:
               filename = obj
               bpy.ops.wm.append(filename=filename, directory=directory)
    
        
        
     
                        
           return{'FINISHED'}
       
       
       
       
         
       
       
       
       
       
       
         
       
       
       
       
       
       
         
       
       
       
       
       
       

    
    



    


def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(MATZOTWOOD)
    bpy.utils.register_class(MATZOTOCEAN)
    bpy.utils.register_class(MATZOTCAR)
    bpy.utils.register_class(MATZOTASPHALT1)
    bpy.utils.register_class(MATZOTASPHALTADVANCED)
    bpy.utils.register_class(MATZOTSPONGEBASIC)
    bpy.utils.register_class(MATZOTDENTEDMETAL)
    bpy.utils.register_class(METALPANEL)
    bpy.utils.register_class(MATZOTFABRICSATIN)
    bpy.utils.register_class(FABRICPANEL)
    bpy.utils.register_class(MATZOTFABRICSATIN2)
    bpy.utils.register_class(MATZOTFABRICUPHOLSTERY)
    bpy.utils.register_class(MATZOTFABRICUPHOLSTERY2)
    bpy.utils.register_class(MATZOTFABRICUPHOLSTERY3)
    bpy.utils.register_class(MATZOTFABRICSILK)
    bpy.utils.register_class(MATZOTFABRICSILK2)
    bpy.utils.register_class(MATZOTFABRICCRUSHED)
    bpy.utils.register_class(MATZOTFABRICCRUSHED2)
    bpy.utils.register_class(MATZOTFABRICLEATHER)
    bpy.utils.register_class(MATZOTFABRICFELT)
    bpy.utils.register_class(MATZOTFABRICST)
    bpy.utils.register_class(MATZOTCOPPER)
    bpy.utils.register_class(MATZOTCOPPER2)
    bpy.utils.register_class(MATZOTCOPPER3)
    bpy.utils.register_class(MATZOTBRASS)
    bpy.utils.register_class(MATZOTBRASS2)
    bpy.utils.register_class(MATZOTSS)
    bpy.utils.register_class(MATZOTSS2)
    bpy.utils.register_class(MATZOTCHROME)
    bpy.utils.register_class(MATZOTDARKMET)
    bpy.utils.register_class(MATZOTALIMINUIM)
    bpy.utils.register_class(MATZOTAM)
    bpy.utils.register_class(MATZOTKEV)
    bpy.utils.register_class(MATZOTLEATH)
    bpy.utils.register_class(MATZOTGM)


def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(MATZOTWOOD)
    bpy.utils.unregister_class(MATZOTOCEAN)
    bpy.utils.unregister_class(MATZOTCAR)
    bpy.utils.unregister_class(MATZOTASPHALT1)
    bpy.utils.unregister_class(MATZOTASPHALTADVANCED)
    bpy.utils.unregister_class(MATZOTSPONGEBASIC)
    bpy.utils.unregister_class(MATZOTDENTEDMETAL)
    bpy.utils.unregister_class(METALPANEL)
    bpy.utils.unregister_class(MATZOTFABRICSATIN)
    bpy.utils.unregister_class(FABRICPANEL)
    bpy.utils.unregister_class(MATZOTFABRICSATIN2)
    bpy.utils.unregister_class(MATZOTFABRICUPHOLSTERY)
    bpy.utils.unregister_class(MATZOTFABRICUPHOLSTERY2)
    bpy.utils.unregister_class(MATZOTFABRICUPHOLSTERY3)
    bpy.utils.unregister_class(MATZOTFABRICSILK)
    bpy.utils.unregister_class(MATZOTFABRICSILK2)
    bpy.utils.unregister_class(MATZOTFABRICCRUSHED)
    bpy.utils.unregister_class(MATZOTFABRICCRUSHED2)
    bpy.utils.unregister_class(MATZOTFABRICFELT)
    bpy.utils.unregister_class(MATZOTFABRICST)
    bpy.utils.unregister_class(MATZOTCOPPER)
    bpy.utils.unregister_class(MATZOTCOPPER2)
    bpy.utils.unregister_class(MATZOTCOPPER3)
    bpy.utils.unregister_class(MATZOTBRASS)
    bpy.utils.unregister_class(MATZOTBRASS2)
    bpy.utils.unregister_class(MATZOTSS)
    bpy.utils.unregister_class(MATZOTSS2)
    bpy.utils.unregister_class(MATZOTCHROME)
    bpy.utils.unregister_class(MATZOTDARKMET)
    bpy.utils.unregister_class(MATZOTALIMINUIM)
    bpy.utils.unregister_class(MATZOTAM)
    bpy.utils.unregister_class(MATZOTKEV)
    bpy.utils.unregister_class(MATZOTLEATH)
    bpy.utils.unregister_class(MATZOTGM)
  
  

if __name__ == "__main__":
    register()

