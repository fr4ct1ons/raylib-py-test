#version 330 core
out vec4 FragColor;
  
in vec4 vertexColor; // the input variable from the vertex shader (same name and same type)  
in vec3 fragNormal;

void main()
{

    FragColor = vec4(1.0, 0.0, 0.7, 1.0);
    float lighting = 1-clamp(dot(fragNormal, vec3(0.5, -0.5, 0.0)), 0.0, 1.0);
    FragColor.xyz = 0.2 + (FragColor.xyz * lighting);
} 