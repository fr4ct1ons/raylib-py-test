#version 330 core
layout (location = 0) in vec3 aPos; // the position variable has attribute position 0
  
in vec2 vertexTexCoord;
in vec3 vertexNormal;

uniform mat4 mvp;
  
out vec4 vertexColor; // specify a color output to the fragment shader
out vec3 fragNormal;

void main()
{
    fragNormal = vertexNormal;
    gl_Position = mvp*vec4(aPos, 1.0); // see how we directly give a vec3 to vec4's constructor
}