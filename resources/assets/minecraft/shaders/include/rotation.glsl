#version 150

#define ROTATION vec2(0.0, 90.0)

mat4 getModelViewMat(vec2 rot) {
  
  float rotX = radians(rot.x);
  float rotY = radians(rot.y);

  mat4 mat = mat4( 
      -cos(rotX), -sin(rotY) * sin(rotX), cos(rotY) * sin(rotX),0.0, 
      0.0, cos(rotY), sin(rotY), 0.0,
      -sin(rotX), sin(rotY) * cos(rotX), -cos(rotY) * cos(rotX), 0.0, 
      0.0, 0.0, 0.0, 1.0);
  return mat;
}

mat4 getFixedModelViewMat() {
  return getModelViewMat(ROTATION);
}